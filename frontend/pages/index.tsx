import { useEffect, useState } from 'react';
import { Container, Button, Form } from 'react-bootstrap';

export default function Home() {
  const [data, setData] = useState<string | null>(null);
  const [link, setLink] = useState<string>('');

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setLink(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    
    // Send the input value to the Flask API
    fetch('http://127.0.0.1:5000/api/search-track', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ link }), // Send the link as JSON
    })
      .then(response => response.json())
      .then(data => {
        setData(data.message); // Assuming your API returns a message
      })
      .catch(error => console.error('Error submitting link:', error));
  };

  return (
    <Container className="mt-5">
      <h1>Next.js + Flask</h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="formLink">
          <Form.Label>Enter a link:</Form.Label>
          <Form.Control 
            type="url" 
            placeholder="Enter your link" 
            value={link} 
            onChange={handleInputChange} 
            required 
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
      {data && <p>{data}</p>} {/* Display fetched data if available */}
    </Container>
  );
}
