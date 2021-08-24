import { StyleSheet } from "react-native"

const styles = StyleSheet.create({
    tab:{
        
        backgroundColor:'white',
        borderTopRightRadius:10,
        borderTopLeftRadius:10,
        height:'7%',
        position:"absolute",
        justifyContent:"center",
        alignContent:"center",

        elevation:0,
        
    },
    shadow:{
        shadowColor:'black',
        shadowOffset:{width:0,height:-10,},
        shadowOpacity:1,
        shadowRadius:3.5,
        elevation:5,}
});

export default styles;
