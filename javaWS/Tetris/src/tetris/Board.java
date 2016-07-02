package tetris;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;

import tetris.Shape.Tetrominoes;

public class Board extends JPanel implements ActionListener {
	
	final int BoardWidth = 10;
	final int BoardHeight = 22;
	
	Timer timer;
	// used to track whether the current piece is still falling
	boolean isFallingFinished = false;
	boolean isStarted = false;
	boolean isPaused = false;
	// Keeps track of the number of lines removed 
	int numLinesRemoved = 0;
	// The current pieces X coord
	int curX = 0;
	// The current pieces Y coord
	int curY = 0;
	JLabel statusbar;
	// The current piece
	Shape curPiece;
	Tetrominoes[] board;
	
	
	public Board(Tetris parent) {
		
		setFocusable(true);
		curPiece = new Shape();
		// sets the timer to fire every 400 ms
		timer = new Timer(400, this);
		timer.start();
		
		statusbar = parent.getStatusBar();
		board = new Tetrominoes[BoardWidth * BoardLength];
		addKeyListener(new TAdapter());
		clearBoard();
	}
	
	public void actionPrefoemed(ActionEvent e) {
		
		if (isFallingFinished) {
			isFallingFinished = false;
			newPiece();
		} else {
			oneLineDown();
		}
	}
	
	int squareWidth() { return (int) getSize().getWidth() / BoardWidth; }
	int squareHeight() { return (int) getSize().getHeight() / BoardWidth; }
	
	Tetrominoes shapeAt(int x, int y) { return board[(y * BoardWidth) + x]; }
	
	public void start() 
	{
		if (isPaused)
			return;
		
		isStarted = true;
		isFallingFinished = false;
		numLinesRemoved = 0;
		clearBoard();
		
		newPiece();
		timer.start();
	}
	
	private void pause() 
	{
		if (!isStarted)
			return;
		
		isPaused = !isPaused;
		if (isPaused) {
			timer.stop();
			statusbar.setText("paused");
		} else {
			timer.start();
			statusbar.setText(String.valueOf(numLinesRemoved));
		}
		repaint();
	}
	
	public void paint(Graphics g) {
		
		super.paint(g);
		
		Dimension size = getSize();
		int boardTop = (int) size.getHeight() - BoardHeight * squareHeight();
		
		
		for(int i=0; i < BoardHeight; i++) {
			for(int j=0; j < BoardWidth; j++) {
				Tetrominoes shape = shapeAt(j, BoardHeight - i -1);
				if (shape != Tetrominoes.NoShape)
					drawSquare(g, 0 + j * squareWidth(), 
							boardTop + i * squareHeight(), shape);
			}
		}
		
		if (curPiece.getShape() != Tetrominoes.NoShape) {
			for(int i = 0; i < 4; i++) {
				int x = curX + curPiece.x(i);
				int y = curY + curPiece.y(i);
				drawSquare(g, 0 + x * squareWidth(), 
						boardTop + (BoardHeight - y - 1) * squareHeight(),
						curPiece.getShape());
			}
		}
	}
	
	private void dropDown() {
		
		int newY = curY;
		
		while (newY > 0) {
			if (!tryMove(curPiece, curX, curY - 1))
				break;
			--newY;
		}
		pieceDropped();
	}
	
	private void clearBoard() {
		
		for (int i = 0; i < BoardHeight * BoardWidth; i++) 
			board[i] = Tetrominoes.NoShape;
	}
	
	private void pieceDropped() {
		
		for (int i = 0; i < 4; i++) {
			int x = curX + curPiece.x(i);
			int y = curY + curPiece.y(i);
			board[(y * BoardWidth) + x] = curPiece.getShape();
		}
		
		removeFullLines();
		
		if (!isFallingFinished)
			newPeice();
	}
	
	private void newPeice() {
		
		curPiece.setRandomShape();
		curX = BoardWidth / 2 + 1;
		curY = BoardHeight - 1 + curPiece.minY();
		
		if (!tryMove(curPeice, curX, curY)) {
			curPiece.setShape(Tetrominoes.NoShape);
			timer.stop()l
			isStarted = false;
			statusbar.setText("gameover :(");
		}
		
	}

}
