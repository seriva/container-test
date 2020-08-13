use serde_json::json;
use warp::Filter;

#[tokio::main]
async fn main() {
    let hello = warp::path("hello")
        .map(|| json!( { "message": "Hello, world!" } ).to_string());

    warp::serve(hello)
        .run(([0, 0, 0, 0], 8080))
        .await;
}
