use std::io::{self, BufRead};

fn main() {
    let mut s = std::collections::HashSet::new();
    let stdin = io::stdin();
    let mut lines = Vec::new();

    for line in stdin.lock().lines() {
        let line = line.expect("Failed to read line");
        lines.push(line.trim().to_string());
    }

    for (row, line) in lines.iter().enumerate() {
        for (col, char) in line.chars().enumerate() {
            if char.is_digit(10) || char == '.' {
                continue;
            }

            for &x in &[row.wrapping_sub(1), row, row + 1] {
                for &y in &[col.wrapping_sub(1), col, col + 1] {
                    if x >= lines.len() as usize ||  y >= lines[x as usize].len() as usize
                        || !lines[x as usize].chars().nth(y as usize).unwrap().is_digit(10)
                    {
                        continue;
                    }
                    let mut y = y;
                    while y > 0 && lines[x as usize].chars().nth(y as usize - 1).unwrap().is_digit(10) {
                        y -= 1;
                    }
                    s.insert((x as usize, y as usize));
                }
            }
        }
    }

    let mut nums = Vec::new();

    for &(x, mut y) in &s {
        let mut a = String::new();
        while y < lines[x].len() && lines[x].chars().nth(y).unwrap().is_digit(10) {
            a.push(lines[x].chars().nth(y).unwrap());
            y += 1;
        }
        nums.push(a.parse::<i32>().expect("Failed to parse integer"));
    }

    println!("{}", nums.iter().sum::<i32>());
}

