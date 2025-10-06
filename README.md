# HackMate 🚀

A comprehensive social platform designed specifically for hackathon enthusiasts to connect, collaborate, and find team members for upcoming hackathons.

## 🌟 Features

### Core Features
- **User Authentication & Authorization** - Secure signup/login with JWT tokens
- **Social Networking** - Follow/unfollow users, view profiles, and connect with fellow hackers
- **Real-time Messaging** - Instant messaging with Socket.IO for seamless communication
- **Post Creation & Sharing** - Share your hackathon experiences, project updates, and ideas
- **Hackathon Discovery** - Browse and discover upcoming hackathons from Devpost
- **Profile Management** - Update profile information, avatar, and personal details
- **Responsive Design** - Modern UI that works seamlessly across all devices

### Advanced Features
- **Real-time Notifications** - Get instant updates on new messages, follows, and interactions
- **Image Upload** - Cloudinary integration for profile pictures and post images
- **Search & Filter** - Find users and hackathons based on various criteria
- **Dark/Light Mode** - Toggle between themes for better user experience
- **Cron Jobs** - Automated tasks for data maintenance and updates

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern React with hooks and functional components
- **Vite** - Fast build tool and development server
- **Chakra UI** - Beautiful and accessible component library
- **Recoil** - State management for React applications
- **React Router DOM** - Client-side routing
- **Socket.IO Client** - Real-time communication
- **Framer Motion** - Smooth animations and transitions
- **Tailwind CSS** - Utility-first CSS framework

### Backend
- **Node.js** - JavaScript runtime environment
- **Express.js** - Web application framework
- **MongoDB** - NoSQL database with Mongoose ODM
- **Socket.IO** - Real-time bidirectional communication
- **JWT** - JSON Web Tokens for authentication
- **bcryptjs** - Password hashing and verification
- **Cloudinary** - Cloud image and video management
- **Cron** - Job scheduling for automated tasks

### Development Tools
- **ESLint** - Code linting and quality assurance
- **Nodemon** - Automatic server restart during development
- **Webdriver Manager** - Automated browser testing

## 📁 Project Structure

```
HackMate/
├── backend/                 # Backend server
│   ├── controllers/        # Route controllers
│   ├── models/            # MongoDB schemas
│   ├── routes/            # API routes
│   ├── middlewares/       # Custom middleware
│   ├── socket/            # Socket.IO configuration
│   ├── cron/              # Scheduled tasks
│   ├── utils/             # Utility functions
│   └── server.js          # Main server file
├── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── pages/         # Page components
│   │   ├── atoms/         # Recoil state atoms
│   │   ├── hooks/         # Custom React hooks
│   │   ├── context/       # React context providers
│   │   └── assets/        # Static assets
│   └── public/            # Public assets
└── extracting/            # Web scraping scripts
    ├── sel.py             # Devpost hackathon scraper
    ├── sel2.py            # Additional scraping utilities
    ├── sel3.py            # Data processing scripts
    └── sel4.py            # Export functionality
```

## 🚀 Installation & Setup

### Prerequisites
- Node.js (v16 or higher)
- MongoDB (local or cloud instance)
- Git

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sujal1804/HackMate.git
   cd HackMate/backend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Environment Configuration**
   Create a `.env` file in the backend directory:
   ```env
   PORT=5000
   MONGODB_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret_key
   CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret
   NODE_ENV=development
   ```

4. **Start the server**
   ```bash
   npm run dev
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

### Web Scraping Setup (Optional)

1. **Navigate to extracting directory**
   ```bash
   cd ../extracting
   ```

2. **Install Python dependencies**
   ```bash
   pip install selenium beautifulsoup4 webdriver-manager
   ```

3. **Run scraping scripts**
   ```bash
   python sel.py
   ```

## 🎯 Usage

### For Users
1. **Sign Up/Login** - Create an account or sign in to access the platform
2. **Complete Profile** - Add your bio, skills, and profile picture
3. **Discover Hackathons** - Browse upcoming hackathons and their details
4. **Connect** - Follow other users and start conversations
5. **Share** - Create posts about your projects and experiences
6. **Chat** - Use real-time messaging to collaborate with team members

### For Developers
- The backend API runs on `http://localhost:5000`
- The frontend development server runs on `http://localhost:5173`
- API documentation is available through the routes in `backend/routes/`

## 🔧 API Endpoints

### Authentication
- `POST /api/users/signup` - User registration
- `POST /api/users/login` - User login
- `POST /api/users/logout` - User logout

### Users
- `GET /api/users/profile/:username` - Get user profile
- `PUT /api/users/update` - Update user profile
- `POST /api/users/follow/:id` - Follow a user
- `DELETE /api/users/follow/:id` - Unfollow a user

### Posts
- `GET /api/posts` - Get all posts
- `POST /api/posts` - Create a new post
- `GET /api/posts/:id` - Get specific post
- `DELETE /api/posts/:id` - Delete a post
- `POST /api/posts/:id/like` - Like/unlike a post

### Messages
- `GET /api/messages/:conversationId` - Get conversation messages
- `POST /api/messages` - Send a message
- `GET /api/messages/conversations` - Get user conversations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sujal** - [Sujal1804](https://github.com/Sujal1804)

## 🙏 Acknowledgments

- Devpost for hackathon data
- Chakra UI team for the amazing component library
- Socket.IO for real-time communication capabilities
- MongoDB for the flexible database solution

## 📞 Support

If you have any questions or need support, please open an issue on GitHub or contact the maintainer.

---

**Happy Hacking! 🎉** 