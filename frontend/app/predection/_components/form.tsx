 "use client";

import React, { FormEvent, useState } from "react";
import { TriangleAlert } from "lucide-react";
import { useSearchParams } from "next/navigation";
import { Input } from "../../components/ui/input";
import { Button } from "../../components/ui/button";
import { Card, CardContent } from "../../components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../../components/ui/select";
 
 




export default function CreateUserForm({setIsOpen , fetchData} :any) {
  const [crop, setEmail] = useState("");
  const [years , setYear] = useState('')
  const params = useSearchParams();
 

 

 

  function onSend(e:FormEvent<HTMLFormElement>) {
 e.preventDefault()
 fetchData(crop , years)

  }
  const handleClick  = () => {
    //  setTimeout(() => {
    //     setIsOpen(false)
    //  }, 750);
  };



  return (
    <div className="">
      <h1 className="font-bold text-lg text-black mb-3">Predection form</h1>
      <Card className="p-6 w-[60%] mx-auto ">
        
        <CardContent className="space-y-5 px-0 pb-0">
          <form onSubmit={onSend} className="space-y-2.5">
            <div className="grid grid-cols-2 gap-2 flex-wrap gap-y-3">
              {/* Dropdown for Year Selection */}
              <Input
              value={crop}
              onChange={(e) => setEmail(e.target.value)}
              className="placeholder:text-black"
              placeholder="Year"
              type="text"
              required
            />

              {/* Dropdown for Crop Selection */}
              <Select  onValueChange={(e)=>{setYear(e)}}>
                <SelectTrigger>
                  <SelectValue placeholder="Crop" />
                </SelectTrigger>
                <SelectContent   className="space-y-1">
                  <SelectItem value="rice">Rice</SelectItem>
                  <SelectItem value="paddy">Paddy</SelectItem>
                  <SelectItem value="wheat">Wheat</SelectItem>
                  <SelectItem value="sorghum">Sorghum</SelectItem>
                  <SelectItem value="sugarcane">Sugarcane</SelectItem>
                </SelectContent>
              </Select>
            </div>
          <Select>
                <SelectTrigger>
                  <SelectValue placeholder="State" />
                </SelectTrigger>
                <SelectContent className="space-y-1">
                  <SelectItem value="MP">Madhaya pradesh</SelectItem>
              
                </SelectContent>
              </Select>


            <Button type="submit" onClick={_=>handleClick()} className="w-full" size="lg">
              Process
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
