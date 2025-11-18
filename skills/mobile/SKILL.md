---
name: mobile-development
description: Master mobile app development with iOS, Android, and cross-platform frameworks. Use when building mobile applications or learning mobile development.
---

# Mobile Development Skill

Comprehensive guide to mobile app development.

## Quick Start

### Swift for iOS
```swift
import SwiftUI

@main
struct ContentView: App {
    var body: some Scene {
        WindowGroup {
            MainView()
        }
    }
}

struct MainView: View {
    @State private var isPresented = false

    var body: some View {
        VStack(spacing: 20) {
            Text("Hello, iOS!")
                .font(.largeTitle)
                .foregroundColor(.blue)

            Button("Tap Me") {
                isPresented.toggle()
            }

            if isPresented {
                Text("Button was tapped!")
                    .transition(.opacity)
            }
        }
        .padding()
    }
}
```

### Kotlin for Android
```kotlin
import androidx.compose.material3.*
import androidx.compose.runtime.*

@Composable
fun HelloAndroid() {
    var count by remember { mutableStateOf(0) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = "Count: $count",
            fontSize = 24.sp
        )

        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}
```

### Flutter with Dart
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Flutter App')),
        body: const CounterWidget(),
      ),
    );
  }
}

class CounterWidget extends StatefulWidget {
  const CounterWidget({Key? key}) : super(key: key);

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int count = 0;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text('Count: $count', style: const TextStyle(fontSize: 24)),
          ElevatedButton(
            onPressed: () => setState(() => count++),
            child: const Text('Increment'),
          ),
        ],
      ),
    );
  }
}
```

### React Native
```javascript
import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>React Native App</Text>
      <Text style={styles.count}>Count: {count}</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={() => setCount(count + 1)}
      >
        <Text style={styles.buttonText}>Increment</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  count: {
    fontSize: 18,
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#007AFF',
    paddingVertical: 12,
    paddingHorizontal: 30,
    borderRadius: 8,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
});
```

## Key Concepts

### iOS Development
- SwiftUI declarative UI
- View state and data flow
- Navigation and routing
- Network requests with URLSession
- Local data persistence (Core Data, SwiftData)
- Permissions and privacy

### Android Development
- Jetpack Compose
- Activity and Fragment lifecycle
- ViewModel and LiveData
- Room database
- WorkManager for background tasks
- Navigation component

### Cross-Platform
- Code sharing between platforms
- Platform-specific code when needed
- Performance considerations
- Testing on multiple devices
- App store deployment

### Mobile Best Practices
- Battery optimization
- Memory management
- Network efficiency
- Responsive design
- Accessibility (VoiceOver, TalkBack)
- User permissions

## Popular Tools

### iOS Development
- Xcode IDE
- Swift Package Manager
- CocoaPods for dependencies
- TestFlight for beta testing

### Android Development
- Android Studio IDE
- Gradle for build
- Firebase for backend services
- Google Play for distribution

### Cross-Platform
- Flutter/Dart
- React Native
- .NET MAUI

## Resources

- [Swift Documentation](https://www.swift.org/documentation/)
- [Android Documentation](https://developer.android.com/docs)
- [Flutter Documentation](https://flutter.dev/docs)
- [React Native Documentation](https://reactnative.dev/docs/)
