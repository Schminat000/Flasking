function delete_note(note_id) {
    // Send a POST request to the server to delete the note
    fetch("/delete-note", {
        method: "POST", // Use the POST method
        body: JSON.stringify({ note_id: note_id}) // Convert note ID to JSON and send it in the request body
    }).then((_res) => {
        // After the request is completed (regardless of the response)
        // Redirect to the home page
        window.location.href = "/";
    });
}