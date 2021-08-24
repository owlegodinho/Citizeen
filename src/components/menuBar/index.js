import {createBottomTabNavigator} from '@react-navigation/bottom-tabs'
import HomeScreen from '../../screens/HomeScreen';
import GreenSpaceProfiles from '../../screens/GreenSpaceProfiles'
import styles from '../menuBar/styles'
import React from 'react';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons'
import MaterialIcons from 'react-native-vector-icons/MaterialIcons'

const Tab = createBottomTabNavigator();

const Menubar = () => {
    return(
        <Tab.Navigator
        screenOptions={{
            tabBarShowLabel:true,
            tabBarStyle:{...styles.tab,
            ...styles.shadow},
            tabBarActiveTintColor:'#4e937a',
            tabBarInactiveTintColor:'#7a7a7a',
        }
            }
        
        
        
            >
            <Tab.Screen 
            name='Map' 
            component={HomeScreen} 
            options={{
                headerShown:false,
                tabBarIcon:({color, size}) => (<MaterialCommunityIcons name='home' color={color} size={size}/>)}}>

            </Tab.Screen>

            <Tab.Screen 
            name='Green Spaces' 
            component={GreenSpaceProfiles} 
            options={{
                headerShown:false,
                tabBarIcon:({color, size}) => (<MaterialIcons name='park' color={color} size={size}/>)} }></Tab.Screen>
        </Tab.Navigator>
            
    )
}

export default Menubar;