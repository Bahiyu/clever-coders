"use client";

import { useRouter } from "next/navigation";
import { ArrowRight, Sparkles } from "lucide-react";
import { Button } from "./components/ui/button";

export default function Home() {
  const router = useRouter()
  const arr = [
    { 
      heading: 'Crop Prediction', 
      description: 'This feature uses advanced machine learning models to forecast crop yields based on historical data, weather conditions, and soil parameters. It helps farmers and agricultural businesses plan for the upcoming season with greater accuracy and efficiency.' 
    },
    { 
      heading: 'Sentiment Analysis', 
      description: 'Analyze social media and news sentiment surrounding agricultural markets and products. This tool helps in understanding public opinion, market trends, and consumer preferences, providing valuable insights for decision-making.' 
    },
    { 
      heading: 'Crop Trend', 
      description: 'Track the historical and emerging trends in crop production, pricing, and demand. This feature offers detailed analytics and visualizations to identify patterns and shifts in agricultural markets, enabling informed planning and investment.' 
    },
    { 
      heading: 'Resource ', 
      description:'Get to know more about crop '
    }
  ];
  
  
  return (
    <>
      <div className="text-white w-full min-h-[248px] flex gap-x-6 p-6 items-center rounded-xl bg-gradient-to-r from-[#2e62cb] via-[#0073ff] to-[#3faff5]">
        <div className="rounded-full size-28 items-center justify-center bg-white/50 hidden md:flex">
          <div className="rounded-full size-20 flex items-center justify-center bg-white">
            <Sparkles className="h-20 text-[#0073ff] fill-[#0073ff]" />
          </div>
        </div>
        <div className="flex flex-col gap-y-2">
          <h1 className="text-xl md:text-3xl font-semibold">
            Predict crop price with us
          </h1>
          <p className="text-xs md:text-sm mb-2">
           Just describe your crop you want to grow and your state.
          </p>
          <Button onClick={()=>{router.push('/predection' , {scroll:false})}} variant="secondary" className="w-[160px]">
            Start pridecting
            <ArrowRight className="size-4 ml-2" />
          </Button>
        </div>
      </div>
      <h1 className="mt-4 text-2xl font-semibold">Features</h1>
      <div className="w-full mt-3 gap-2 grid grid-cols-2">
 

 {arr.map(el=>{
  return <>
       <div className="rounded-lg flex flex-col p-6 gap-3 border border-gray-300 shadow-sm aspect-[1/0.4] shadow-lg transition-transform duration-300 transform hover:scale-[1.01]">
      <h1 className="font-bold text-black text-xl">{el.heading}</h1> 
      <p className="text-base text-gray-800 font-medium">
        {el.description}
      </p>
    </div>
  
  </>
 })
}

      </div>
    </>
  );
}
