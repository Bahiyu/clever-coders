 "use client";

import React, { useState } from "react";
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
 
import MultipleSelector, { Option } from '../../components/ui/multiple-selector';
import { SelectLabel } from "@radix-ui/react-select";

const OPTIONS: Option[] = [
  { label: 'nextjs', value: 'nextjs' },
  { label: 'React', value: 'react' },
  { label: 'Remix', value: 'remix' },
  { label: 'Vite', value: 'vite' },
  { label: 'Nuxt', value: 'nuxt' },
  { label: 'Vue', value: 'vue' },
  { label: 'Svelte', value: 'svelte' },
  { label: 'Angular', value: 'angular' },
  { label: 'Ember', value: 'ember', disable: true },
  { label: 'Gatsby', value: 'gatsby', disable: true },
  { label: 'Astro', value: 'astro' },
];





export default function CreateUserForm() {
  const [email, setEmail] = useState("");
  const params = useSearchParams();
  const error = params.get("error");

  // State to manage selected years
 
  const [selectedOptions, setSelectedOptions] = useState<string[]>([])

 

  function onSend() {
    // Handle form submission
  }
  const handleSelect = (value: string) => {
    setSelectedOptions((prev) =>
      prev.includes(value) ? prev.filter((item) => item !== value) : [...prev, value]
    );
  };

  return (
    <div>
      <h1 className="font-bold text-lg text-black mb-3">Predection form</h1>
      <Card className="p-6 md:w-[40vw]">
        
        <CardContent className="space-y-5 px-0 pb-0">
          <form onSubmit={onSend} className="space-y-2.5">
          <Select>
                <SelectTrigger>
                  <SelectValue placeholder="State" />
                </SelectTrigger>
                <SelectContent className="space-y-1">
                  <SelectItem value="MP">Madhaya pradesh</SelectItem>
              
                </SelectContent>
              </Select>

            <div className="flex w-full flex-wrap gap-y-3">
              {/* Dropdown for Year Selection */}
              <Input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="placeholder:text-black"
              placeholder="Year"
              type="text"
              required
            />

              {/* Dropdown for Crop Selection */}
              <Select>
                <SelectTrigger>
                  <SelectValue placeholder="Crop" />
                </SelectTrigger>
                <SelectContent className="space-y-1">
                  <SelectItem value="Rice">Rice</SelectItem>
                  <SelectItem value="Paddy">Paddy</SelectItem>
                  <SelectItem value="Wheat">Wheat</SelectItem>
                  <SelectItem value="Sorghum">Sorghum</SelectItem>
                  <SelectItem value="Sugarcane">Sugarcane</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <Button type="submit" className="w-full" size="lg">
              Send
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
