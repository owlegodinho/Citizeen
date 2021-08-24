import {NavigationContainer} from '@react-navigation/native';
import MenuBar from './src/components/menuBar/index';
import React, {useEffect} from 'react';
import {StatusBar, PermissionsAndroid, Platform, } from 'react-native';
import HomeMap from './src/components/HomeMap';
import { initialWindowMetrics, SafeAreaProvider } from 'react-native-safe-area-context';

navigator.geolocation = require('@react-native-community/geolocation');

const App = () =>{

  const androidPermission = async() => {
    try {

    const granted = await PermissionsAndroid.request(
      PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
      {
        title: "Uber",
        message:
          "Citizeen needs access to your location ",
        buttonNeutral: "Ask Me Later",
        buttonNegative: "Cancel",
        buttonPositive: "OK",
      }
      );
      if (granted === PermissionsAndroid.RESULTS.GRANTED) {
        console.log("You can use the Location");
      } else {
        console.log("Location permission denied");
      }
    } catch (err) {
      console.warn(err);
    }
  };
  useEffect(()=>{
    if (Platform.OS === 'android'){
      androidPermission();
      
    }
    
  })
  return(
    <SafeAreaProvider initialMetrics={initialWindowMetrics}>
      <NavigationContainer>
      <StatusBar></StatusBar>
      <MenuBar/>
    </NavigationContainer>
    </SafeAreaProvider>
  )
}
export default App;