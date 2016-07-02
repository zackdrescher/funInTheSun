package tetris;

import java.util.Random;
import java.lang.Math;

public class Shape {
	
	//The different kinds of shapes a shape can be 
	enum Tetrominoes { NoShape, ZShape, SShape, LineShape, TShape, 
		SquareShape, LShape, MirrLShape}
	
	// The shape of this peice
	private Tetrominoes peiceShape;
	// The coordinate location of this peice 
	private int coords[][];
	// The orientaion of this peice
	private int[][][] coordsTable;
	
	

}
