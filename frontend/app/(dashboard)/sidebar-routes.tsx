"use client";

import { 
TreePine,
  Home, 

} from "lucide-react";
import { usePathname } from "next/navigation";

 

import { Button } from "../components/ui/button";
import { Separator } from "../components/ui/separator";

import { SidebarItem } from "./sidebar-item";

export const SidebarRoutes = () => {
  

  const pathname = usePathname();
 


  

  return (
    <div className="flex flex-col gap-y-4 flex-1">
    
      <ul className="flex flex-col gap-y-1 px-3">
        <SidebarItem
          href="/"
          icon={Home}
          label="Home"
          isActive={pathname === "/"}
        />
          <SidebarItem
          href="/predection"
          icon={TreePine}
          label="Predection"
          isActive={pathname === "/predection"}
        />
      </ul>
       
      <ul className="flex flex-col gap-y-1 px-3">
        {/* <SidebarItem
          href={pathname}
          icon={CreditCard}
          label="Billing"
          onClick={onClick}
        />
        <SidebarItem
          href="mailto:support@codewithantonio.com"
          icon={MessageCircleQuestion}
          label="Get Help"
        /> */}
      </ul>
    </div>
  );
};
