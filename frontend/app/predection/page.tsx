'use client'
import React, { useState } from 'react'
import DataCharts from './_components/data-charts'
import CropForm from './_components/form'
import axios from 'axios'

export default function  Predection() {

    const [isOpen , setIsOpen] = useState(true)

    const [data ,setData] = useState([])

    const fetchData = async(crop :any , years :any) =>{
         
        const repos = await axios.post('api/predection' , {
           crop , years
          })
     
        const data = await repos.data
        console.log(data)
        const arrayOfObjects = data.data.modelData.map(([year, price]:any) => ({
            year,
            price
          }));
      setData(arrayOfObjects)
      setIsOpen(false)
    }

  return (
    <div> 
  
       <CropForm setIsOpen={setIsOpen} fetchData={fetchData} />
{ !isOpen && <div className='grid gap-2 mt-10'>
          <h1 className='text-black font-bold textxl '>Graph reprenstation of price</h1>
        <DataCharts data={data} />
</div>}
    </div>
  )
}
