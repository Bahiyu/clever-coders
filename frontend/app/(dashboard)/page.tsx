"use client";

import { useRouter } from "next/navigation";
import { ArrowRight, Sparkles } from "lucide-react";
import { Button } from "../components/ui/button";

export default function Home() {
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
          <Button variant="secondary" className="w-[160px]">
            Start pridecting
            <ArrowRight className="size-4 ml-2" />
          </Button>
        </div>
      </div>
    </>
  );
}
