import { StyleSheet,Dimensions } from 'react-native';

const styles = StyleSheet.create({
    mapContainer:{
        height:Dimensions.get('screen').height,
        width:Dimensions.get('screen').width,
        flex:1
    },
    container:{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        flex:1,
       },
    gpsButtonContainer:{
        backgroundColor:'white',
        position:'absolute',
        right:'4%',
        top:'30%',
        height:45,
        width:45,
        borderRadius:15,
        justifyContent:'center',
        alignItems:'center',
        zIndex:100,
        
    },


});

export default styles;