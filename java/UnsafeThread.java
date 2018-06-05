package com.jfw.thread.unsafe;

public class UnsafeThread implements Runnable {
	
	private volatile int count = 0;

	public void run() {
		for (int i = 0; i < 1000; i++) {
			Math.hypot(Math.pow(92564812, i), Math.cos(i));
		}
		System.out.println("线程名"+Thread.currentThread());
		count++;
	}
	
	public int	 getCount() {
		return this.count;
	}
}
