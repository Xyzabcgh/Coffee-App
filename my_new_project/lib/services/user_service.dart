import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class UserService {
  final String _apiBaseUrl =
      "http://10.0.2.2:5000"; // Replace with your Flask backend base URL

  // Fetch user details from the API and cache them
  Future<Map<String, dynamic>> fetchUserDetails(String token) async {
    try {
      final response = await http.get(
        Uri.parse("$_apiBaseUrl/auth/user/details"), // Match Flask's route
        headers: {
          'Authorization': 'Bearer $token', // Include the token
          'Content-Type': 'application/json',
        },
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        await _cacheUserData(data);
        return data;
      } else if (response.statusCode == 401) {
        throw Exception("Unauthorized. Please log in again.");
      } else {
        throw Exception(
            "Failed to fetch user details. Status code: ${response.statusCode}");
      }
    } catch (error) {
      throw Exception("An error occurred: $error");
    }
  }

  // Cache the user data locally using SharedPreferences
  Future<void> _cacheUserData(Map<String, dynamic> userData) async {
    final prefs = await SharedPreferences.getInstance();
    prefs.setString('user', json.encode(userData));
  }

  // Retrieve the cached user data
  Future<Map<String, dynamic>> getCachedUserData() async {
    final prefs = await SharedPreferences.getInstance();
    final userData = prefs.getString('user');
    if (userData != null) {
      return json.decode(userData);
    } else {
      return {}; // Return an empty map if no cached data exists
    }
  }

  // Clear the cached user data
  Future<void> clearCachedData() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('user'); // Removes the cached user data
  }
}
