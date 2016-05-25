extern crate time;

use std::thread;
use std::time::*;
use std::sync::{Mutex, Arc};

struct Philosopher {
	name: String,
	left: usize,
	right: usize,
}

impl Philosopher{
	fn new(name: &str, left: usize, right: usize) -> Philosopher{
		Philosopher{
			name: name.to_string(),
			left: left,
			right: right,
		}
	}

	fn eat(&self, table: &Table) {
		let _left = table.chopsticks[self.left].lock().unwrap();
		println!("{:?}: {} gets his first chopstick: chopstick{}", time::get_time(), self.name, self.left);

		thread::sleep(Duration::from_millis(150));

		let _right = table.chopsticks[self.right].lock().unwrap();
		let start = time::get_time();
		println!("{:?}: {} gets his second chopstick: chopstick{} and starts eating", start, self.name, self.right);

		thread::sleep(Duration::from_millis(1000));
		let end = time::get_time();
		println!("{:?}: {} ate up", end, self.name);
	}
}

struct Table {
	chopsticks: Vec<Mutex<()>>,
}

fn main()
{
	let table = Arc::new(Table{ chopsticks: vec![
		Mutex::new(()),
		Mutex::new(()),
		Mutex::new(()),
		Mutex::new(()),
		Mutex::new(()),
	]});

	let philosophers = vec![
		Philosopher::new("Philosopher 1", 0, 1),
		Philosopher::new("Philosopher 2", 1, 2),
		Philosopher::new("Philosopher 3", 2, 3),
		Philosopher::new("Philosopher 4", 3, 4),
		Philosopher::new("Philosopher 5", 0, 4),
	];

	let handles: Vec<_> = philosophers.into_iter().map(|p| {
		let	table = table.clone();
		thread::spawn(move||{
			p.eat(&table);
		})
	}).collect();
	
	for h in handles{
		h.join().unwrap();
	}
}
