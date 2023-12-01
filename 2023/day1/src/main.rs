use util::get_lines;
fn main() {
    println!("Current working directory: {:?}", std::env::current_dir());
    get_lines(|lines| {
        println!("{:?}",lines);
    })
}
