use serde::Deserialize;
use std::collections::HashMap;
use std::fs::File;
use std::io::Read;
use util::get_file_name;
use regex::Regex;


#[derive(Debug, Deserialize)]
struct Entry {
    #[serde(flatten)]
    rows: HashMap<String,Vec<String>>,
}
fn parse_color_string(color_string: &str) -> Vec<(usize,String)> {
    let re = Regex::new(r"(\d+) (\w+)").unwrap();
    re.captures_iter(color_string)
        .filter_map(|cap| {
            let count = cap[1].parse::<usize>().ok()?;
            let color = cap[2].to_string();
            Some((count,color))
        })
    .collect()
}
fn calc(game:Vec<String>) -> usize {
    let mut max =[0;3];
    for turn in game {
        for (count,color) in &parse_color_string(&turn){
            match color.as_str() {
                "red" => {
                    if max[0] < *count {max[0] = *count;}
                },
                "blue" => {
                    if max[1] < *count {max[1] = *count;}
                },
                "green" => {
                    if max[2] < *count {max[2] = *count;}
                },
                _=> {
                }
            }

        };
             
    }
    max.iter().fold(1,|acc,&x| acc*x)
}
fn main() {
    let fpath = get_file_name();
    let mut file = File::open(fpath).expect("Unable to open this file");
    let mut data = String::new();
    file.read_to_string(&mut data).expect("unable to read file");
    let parsed: Entry = serde_json::from_str(&data).expect("Failed to parse json");
    let mut sum = 0;
    for a in parsed.rows{
        sum+=calc(a.1);
    }
    println!("{sum}");
}
