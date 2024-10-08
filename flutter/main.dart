import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

const key = '';
const base_url = '';

void main() {
  runApp(const ConfettiCannonApp());
}

Future<void> fireConfettiCannon() async {
  final url = Uri.https(base_url, '/fire_cannon', { 'key': key });

  try {
    final response = await http.post(url, headers: {
        "ngrok-skip-browser-warning": "yes",
        "User-Agent": "Pieces-Confetti",
    });
    final statusCode = response.statusCode;
    if (statusCode != 200) { throw Exception("Status code $statusCode");}
  } catch (e) {
    print('Error occurred while firing confetti cannon: $e');
  }
}

class ConfettiCannonApp extends StatelessWidget {
  const ConfettiCannonApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: ConfettiCannonScreen(),);
  }
}

class ConfettiCannonScreen extends StatefulWidget {
  const ConfettiCannonScreen({super.key});

  @override
  _ConfettiCannonScreenState createState() => _ConfettiCannonScreenState();
}

class _ConfettiCannonScreenState extends State<ConfettiCannonScreen> {
  bool _isLoading = false;

  Future<void> _handleButtonPressed() async {
    setState(() { _isLoading = true; });
    await fireConfettiCannon();
    setState(() { _isLoading = false; });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: _isLoading
            ? const CircularProgressIndicator()
            : ElevatedButton(
                onPressed: _isLoading ? null : () async { await _handleButtonPressed(); },
                child: const Text('🎉 Confetti 🎉', style: TextStyle(fontSize: 36)),
              ),
      ),
    );
  }
}