import React, { Component, useState, createElement } from 'react';
import { View, Text, TouchableOpacity, Touchable } from 'react-native';
import {Polygon, PROVIDER_GOOGLE,Marker} from 'react-native-maps';
import styles from './styles';
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';
import Geolocation from '@react-native-community/geolocation';
import polygons from '../../assets/data/coordinates'
import MapView from 'react-native-map-clustering'


navigator.geolocation = require('@react-native-community/geolocation');


const HomeMap = (props) => {

    const [region, setRegion] = useState({
        latitude:39.399872,
        longitude:-8.224454,
        latitudeDelta:5,
        longitudeDelta:5,
        })

    const onPress = (selectedRegion) => {
            setRegion(selectedRegion)
            };

    {/*const [markerArr, setMarkerArr] = useState(polygons)*/}
    
    const renderMarker = () => {return polygons.map((points)=>console.log(points.POI))}
    const mapRef = React.createRef();
    const animateMap = () =>{
        Geolocation.getCurrentPosition(position =>{
            mapRef.current.animateToRegion({
                latitude:position.coords.latitude, 
                longitude:position.coords.longitude,
                latitudeDelta:0.01,
                longitudeDelta:0.01,

            },2000),console.log(position.coords.latitude, position.coords.longitude,) }
        )

    };


    return (
        <>
            <View style={styles.container}>

            
                <MapView
                    ref={mapRef}
                    style={styles.mapContainer}
                    provider={PROVIDER_GOOGLE}
                    showsUserLocation={true}
                    mapType={'hybrid'}
                    showsCompass={true}
                    showsMyLocationButton={false}
                    initialRegion={{
                        latitude:39.399872,
                        longitude:-8.224454,
                        latitudeDelta:5,
                        longitudeDelta:5,
                        }}
                    onRegionChangeComplete={(selectedRegion) => onPress(selectedRegion)}
                
                >
                    
            {polygons.map((polygon)=> region.latitudeDelta <= 0.030 ? <Polygon
                key={polygon.id}               
                coordinates={polygon.area}
                fillColor={'rgba(42, 157, 143, 0.35)'}
                tappable={true}
                strokeColor={'#edf6f9'}
                strokeWidth={3}
                onPress={()=>renderMarker()}
                />  : <Marker
                        key={polygon.id}
                        coordinate={polygon.point} 
                
                />)}
            
            
            </MapView>
                
            </View>
            <View style={styles.gpsButtonContainer}>
                <TouchableOpacity onPress={animateMap}>
                <MaterialIcons name={'gps-fixed'} size={25} color={'#4e937a'}/>
                </TouchableOpacity>
            </View>
            
        </>
            

    )
}

export default HomeMap;
