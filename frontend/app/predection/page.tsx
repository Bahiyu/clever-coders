import React from 'react'
import DataCharts from './_components/data-charts'
import CropForm from './_components/form'

export default function  Predection() {
  return (
    <div> 
  
       <CropForm/>
<div className='grid gap-2 mt-10'>
          <h1 className='text-black font-bold textxl '>Graph reprenstation of price</h1>
        <DataCharts />
</div>
    </div>
  )
}
