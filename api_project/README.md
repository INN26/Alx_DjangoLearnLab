## Authentication & Permissions
Our API uses Token Authentication.

### **How to Obtain a Token**
1. Send a `POST` request to `/api-token-auth/` with your username and password.
2. You'll receive a token like this:
   ```json
   {
       "token": "your_generated_token_here"
   }