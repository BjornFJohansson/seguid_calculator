fn minimal_rotation(s: &str) -> String {
    let chars: Vec<char> = s.chars().collect();
    let n = chars.len();
    let mut i = 0;
    let mut j = 1;
    let mut k = 0;

    while i < n && j < n && k < n {
        let cmp = chars[(i + k) % n].cmp(&chars[(j + k) % n]);
        if cmp == std::cmp::Ordering::Equal {
            k += 1;
        } else {
            if cmp == std::cmp::Ordering::Greater {
                i += k + 1;
            } else {
                j += k + 1;
            }
            if i == j {
                j += 1;
            }
            k = 0;
        }
    }

    let start = std::cmp::min(i, j);
    chars[start..].iter().collect::<String>() + &chars[..start].iter().collect::<String>()
}

fn main() {
    let s = "duvalduval";
    let minimal_rotation = minimal_rotation(s);
    println!("Minimal Rotation: {}", minimal_rotation);
}
