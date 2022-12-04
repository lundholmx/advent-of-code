use std::{
    env, error,
    fs::File,
    io::{self, BufRead, BufReader},
    process,
};

fn main() -> Result<(), Box<dyn error::Error>> {
    let args = env::args();
    let infile = match args.len() {
        2 => args.skip(1).next().unwrap(),
        _ => {
            eprintln!("expected 1 argument");
            process::exit(1);
        }
    };

    let lines = get_input(&infile)?;
    for line in lines {
        println!("{}", line);
    }
    Ok(())
}

fn get_input(filepath: &str) -> Result<Vec<String>, io::Error> {
    let file = File::open(filepath)?;
    let reader = BufReader::new(file);
    let mut lines = Vec::new();
    for line in reader.lines() {
        let l = line?;
        lines.push(l);
    }
    Ok(lines)
}
