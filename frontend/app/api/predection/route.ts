
 import axios from  'axios'
import { NextResponse } from 'next/server'


export  async function POST(req: Request, res: Response){
    const { years ,crop } = await req.json()
 
   
   try {
     const repos = await axios.post('http://192.168.48.113:8000/about/', { "years" : crop , "crop" : years})
     
         const data = await repos.data
         console.log(data)
         return NextResponse.json({data} , {status:200})

   } catch (error) {

    return new NextResponse("internal server error" , {status:402})
    
   }
}