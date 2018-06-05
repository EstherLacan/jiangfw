package com.jfw.thread.unsafe;

public class Counter implements Runnable{
	volatile int count = 0;
	
	public int	 getCount() {
		return this.count;
	}

	public void run() {
		// TODO Auto-generated method stub
	}
}
