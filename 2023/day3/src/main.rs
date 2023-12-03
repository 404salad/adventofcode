use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let lines: Vec<String> = stdin.lock().lines().map(|line| line.unwrap()).collect();

    let mut t: Vec<i32> = Vec::new();

    for (row, line) in lines.iter().enumerate() {
        for (col, char) in line.chars().enumerate() {
            if char != '*' {
                continue;
            }

            let mut s = std::collections::HashSet::new();

            for x in [row as i32 - 1, row as i32, row as i32 + 1].iter() {
                for y in [col as i32 - 1, col as i32, col as i32 + 1].iter() {
                    let x = *x as usize;
                    let y = *y as usize;

                    if x >= lines.len() || y >= lines[x].len() || !lines[x].chars().nth(y).unwrap().is_digit(10) {
                        continue;
                    }

                    let mut y_temp = y;
                    while y_temp > 0 && lines[x].chars().nth(y_temp - 1).unwrap().is_digit(10) {
                        y_temp -= 1;
                    }
                    s.insert((x, y_temp));
                }
            }

            if s.len() != 2 {
                continue;
            }

            let mut nums = Vec::new();

            for (x, y) in s.iter() {
                let mut a = String::new();
                let mut y_temp = *y;
                while y_temp < lines[*x].len() && lines[*x].chars().nth(y_temp).unwrap().is_digit(10) {
                    a.push(lines[*x].chars().nth(y_temp).unwrap());
                    y_temp += 1;
                }
                nums.push(a.parse::<i32>().unwrap());
            }

            t.push(nums[0] * nums[1]);
        }
    }

    println!("{}", t.iter().sum::<i32>());
}

