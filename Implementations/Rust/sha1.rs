use sha1::Digest;

fn sha1_digest(input: &str) -> String {
    let mut hasher = sha1::Sha1::new();
    hasher.update(input.as_bytes());
    let result = hasher.finalize();

    let hex_string = result
        .iter()
        .map(|byte| format!("{:02x}", byte))
        .collect::<String>();

    hex_string
}

fn main() {
    let input = "Hello, world!";
    let digest = sha1_digest(input);
    println!("SHA-1 digest: {}", digest);
}
