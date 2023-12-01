use util::get_lines;

fn replace_digits(input: &str) -> String {
    let replaced = input
        .replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "4")
        .replace("five", "5e")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "e8t")
        .replace("nine", "9");

    replaced
}
fn getsum(word: &str) -> u32 {
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
        let mut sum = 0;
        for word in lines {
            sum+=getsum(&replace_digits(word));
        }
        println!("{sum}");
    });
}
