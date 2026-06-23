# SSL Setup

Since no production domain is available, SSL is not configured.

Production approach:

- Point domain to VPS
- Install Certbot
- Generate Let's Encrypt certificate
- Configure NGINX to listen on port 443
- Redirect HTTP to HTTPS