package com.jfw.thread;

import com.jfw.thread.safe.SynCounter;
import com.jfw.thread.unsafe.UnsafeThread;

public class TestThread {

	static int value = 1000;
	static int loops = 0;
	public static void main(String[] args) throws InterruptedException  {
//		testUnsafeThread();
		testSafeThread();
	}
	
	public static void  testUnsafeThread() throws InterruptedException{
		ThreadGroup tg = Thread.currentThread().getThreadGroup();
		while (loops++ < 50) {
			UnsafeThread run = new UnsafeThread();
			for (int i = 0; i < value; i++) {
				new Thread(run, "线程" + loops + "-" + i).start();
			}
			do {
				Thread.sleep(15);
			} while (tg.activeCount() != 1);

			if (run.getCount() != value) {
				System.out.println("循环到" + loops + "次，出现线程不安全");
				System.out.println("最终值为" + run.getCount());
				System.exit(0);
			}

		}
		System.out.println("线程安全");
	}
	
	public static void  testSafeThread() throws InterruptedException{
		ThreadGroup tg = Thread.currentThread().getThreadGroup();
		while (loops++ < 50) {
			SynCounter run = new SynCounter();
			for (int i = 0; i < value; i++) {
				new Thread(run, "线程" + loops + "-" + i).start();
			}
			do {
				Thread.sleep(15);
			} while (tg.activeCount() != 1);

			if (run.getCount() != value) {
				System.out.println("循环到" + loops + "次，出现线程不安全");
				System.out.println("最终值为" + run.getCount());
				System.exit(0);
			}

		}
		System.out.println("线程安全");
	}

}
