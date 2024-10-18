import React from "react";
import { Sidebar } from "./sidebar";

type props = { children: React.ReactNode };

export default function layout({ children }: props) {
  return  <>
  <div className="bg-muted h-full">
      <Sidebar />
      <div className="lg:pl-[300px] flex flex-col h-full">
        {/* <Navbar /> */}
        <main className="bg-white flex-1 overflow-auto p-8 lg:rounded-tl-2xl">
          {children}
        </main>
      </div>
    </div>
  </>
  
}
