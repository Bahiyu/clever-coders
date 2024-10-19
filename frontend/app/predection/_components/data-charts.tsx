import { BarChart } from '@mui/x-charts/BarChart';


const chartSetting = {
    yAxis: [
      {
        label: 'Price',
    
      },
    ],
    width: 900,
    height: 400,
    
  };

  const ricePrices = [
    { year: 2019, price: 500 },
    { year: 2020, price: 520 },
    { year: 2021, price: 540 },
    { year: 2022, price: 580 },
    { year: 2023, price: 600 },
  ];
  

export default function DataCharts(){
    return <div className='flex w-full justify-center items-center'>
    <BarChart
   
    dataset={ricePrices}
    xAxis={[{ scaleType: 'band', dataKey: 'year' }]}
    series={[{ dataKey: 'price', label: 'Rice' }]}
    layout="vertical"
    {...chartSetting}
/>
    


    </div>
}