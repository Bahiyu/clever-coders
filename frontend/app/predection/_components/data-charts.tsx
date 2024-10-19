import { BarChart } from '@mui/x-charts/BarChart';


const chartSetting = {
    yAxis: [
      {
        label: 'Price per quantal',
    
      },
    ],
    width: 900,
    height: 400,
    
  };

  
  

export default function DataCharts({data}:any){
    return <div className='flex w-full justify-center items-center'>
    <BarChart
   
    dataset={data}
    xAxis={[{ scaleType: 'band', dataKey: 'year' }]}
    series={[{ dataKey: 'price', label: 'Crop' }]}
    layout="vertical"
    {...chartSetting}
/>
    


    </div>
}