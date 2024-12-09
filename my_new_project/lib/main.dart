import 'package:flutter/material.dart';

import 'screens/index.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Coffee App',
      theme: ThemeData(primarySwatch: Colors.brown),
      initialRoute: '/login',
      routes: {
        '/login': (context) => const LoginScreen(),
        '/signup': (context) => const SignUpScreen(),
        '/home': (context) => const HomePage(),
        '/cart': (context) => CartPage(),
        '/profile': (context) => ProfilePage(),
      },
    );
  }
}
