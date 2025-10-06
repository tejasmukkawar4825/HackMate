import jwt from "jsonwebtoken";

const generateTokenAndSetCookie = (userId, res) => {
  const token = jwt.sign({ userId }, process.env.JWT_SECRET, {
    expiresIn: "15d",
  });

  res.cookie("jwt", token, {
    httpOnly: true, // more secure Prevents client-side JavaScript from accessing the cookie (enhances security).
    maxAge: 15 * 24 * 60 * 60 * 1000, // 15 days
    sameSite: "strict", // Prevents CSRF (Cross-Site Request Forgery) attacks by ensuring the cookie is only sent with requests from the same origin.
  });

  return token;
};

export default generateTokenAndSetCookie;
