import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter_secure_storage/flutter_secure_storage.dart'; // For storing token securely

class AuthService {
  final FlutterSecureStorage _storage =
      const FlutterSecureStorage(); // Secure storage instance

  Future<Map<String, dynamic>> signup(
      String username, String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse("http://10.0.2.2:5000/auth/signup"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode(
            {"username": username, "email": email, "password": password}),
      );

      if (response.statusCode == 200) {
        return jsonDecode(response.body); // Successful signup
      } else {
        // Handle errors based on the response status code
        return {"error": "Signup failed: ${response.body}"};
      }
    } catch (error) {
      return {"error": "An error occurred: $error"};
    }
  }

  Future<Map<String, dynamic>> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse("http://10.0.2.2:5000/auth/login"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"email": email, "password": password}),
      );
      print("statuscode");
      print(response.body);
      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        String token =
            responseData['access_token']; // Assuming the token is returned here

        // Store token securely after successful login
        await _storage.write(key: 'auth_token', value: token);
        String? storedToken = await _storage.read(key: 'auth_token');
        print("Stored token: $storedToken");
        return responseData; // Return successful login data
      } else {
        // Handle errors based on the response status code
        return {"error": "Login failed: ${response.body}"};
      }
    } catch (error) {
      return {"error": "An error occurred: $error"};
    }
  }

  // Method to get the stored token (useful for future requests)
  Future<String?> getToken() async {
    return await _storage.read(key: 'auth_token');
  }

  // Method to logout (clear token)
  Future<void> logout() async {
    await _storage.delete(key: 'auth_token');
  }
}
