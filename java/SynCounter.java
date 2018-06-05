package com.jfw.thread.safe;

public class SynCounter implements Runnable {
	private int count = 0;

	public void run() {
		synchronized (this) {
			for (int i = 0; i < 1000; i++) {
				Math.hypot(Math.pow(92564812, i), Math.cos(i));
			}
			System.out.println("线程名" + Thread.currentThread());
			count++;
		}
	}

	public int getCount() {
		return this.count;
	}
}
