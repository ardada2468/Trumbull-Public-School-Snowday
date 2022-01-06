
import React from "react";
import { createClient } from '@supabase/supabase-js'
import Snowfall from "react-snowfall";

const supabase = createClient("https://aytmwwzjtowgqnkvojtr.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjQxNDA2NTU3LCJleHAiOjE5NTY5ODI1NTd9.wZ7S4A_CPhJ2oiHrkrdg1Pdmy-KOLdG4ysvJg5phms0");

export default class Snow extends React.Component{

    state={
        data:[] 
    }

fetchData = async () => {
    const { data: Snowday, error: errorinfo } = await supabase.from('Snowday').select('*').order('id', true)
      console.table(Snowday)
        this.setState({data:Snowday})
      console.table(Snowday)
      console.table(this.state.data)
    } 
    
    constructor(props) {
        super(props);
        this.state = { data: undefined } ;
        //set state by fetching data
        this.fetchData();

      }

componentDidMount(){
    console.log("componentdid moutn")
    this.fetchData().then(console.table(this.state));
}

render(){
   
        if(this.state.data!=undefined){
            return( 
            <div className={"main"}>
                    {this.state.data[0].isHappy ? <Snowfall></Snowfall> : <div></div>}
            <h1 className={"typeDay"}>
                
                {this.state.data[0].typeDay}
            </h1>
            <h3>
                {this.state.data[0].websiteText}
            </h3>
            <p>
               last updated on:  {this.state.data[0].created_at}
            </p>
            </div>
            )
        }
        else{ 
            return(
                <h1>loading...</h1>
            )   
        }
       

}
}