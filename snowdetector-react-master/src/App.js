
import { useState, useEffect } from 'react'

import { createClient } from '@supabase/supabase-js'
import React, { useLayoutEffect } from "react";
import Snow from './components/snow';
import Snowfall from 'react-snowfall';

const meta = {
  title: 'Trumbull Public School snow day',
  description: 'Created by Arnav Dadarya',
  meta: {
      charset: 'utf-8',
      name: {
          keywords: 'Arnav Dadarya, Trumbull High School Snow,Snow,Trumbull Public Schools, Trumbull, Snow Day'
      }
  }
}

export default function Home() {
  
  
  return (
    
    <div className={"mainDiv"}>
      <main className={"main"}>
        {/* <Snowfall></Snowfall> */}
        <Snow></Snow>
      </main> 

      <footer className={"footer"}>
        <a>
          Created by {' Arnav Dadarya'}
        </a>
      </footer>
    </div>
  )
}
