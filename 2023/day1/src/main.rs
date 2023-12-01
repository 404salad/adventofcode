use util::get_lines;
fn getsum(word: &str) -> u32 {
    println!("got input {}", word);
    if word.is_empty() {return 0};
    let mut i = 0;
    let mut j = word.len()-1;
    for a in word.chars() {
        if a.is_digit(10) {break;}
        i+=1;
    }
    for a in word.chars().rev() {
        if a.is_digit(10) {break;}
        j-=1;
    }
    let mut ret = String::from("");
    ret.push(word.chars().nth(i).unwrap());
    ret.push(word.chars().nth(j).unwrap());
    ret.parse::<u32>().unwrap()
    
}
fn main() {
    get_lines(|lines| {
        for word in lines {
            println!("{} {}", word, getsum(word));
        }
    })
}
