
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

OLD = (
    '<div class="relative aspect-square cursor-zoom-in group overflow-hidden">'
    '<div class="relative w-full h-full" style="opacity: 1;">'
    '<img alt="Laptop Lenovo frontal" class="w-full h-full object-contain p-8 transition-transform duration-200" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg" style=""></div>'
    '<div class="absolute top-4 right-4 bg-white/80 backdrop-blur-sm rounded-lg px-3 py-2 flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">'
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-zoom-in w-4 h-4 text-neutral-600" aria-hidden="true">'
    '<circle cx="11" cy="11" r="8"></circle><line x1="21" x2="16.65" y1="21" y2="16.65"></line><line x1="11" x2="11" y1="8" y2="14"></line><line x1="8" x2="14" y1="11" y2="11"></line></svg>'
    '<span class="text-xs font-medium text-neutral-700">Hover para zoom</span></div>'
    '<div class="absolute bottom-4 left-4 bg-black/60 backdrop-blur-sm rounded-lg px-3 py-1.5 flex items-center">'
    '<span class="text-[10px] uppercase tracking-wider text-white/80 leading-none">Imagen referencial</span></div>'
    '<div class="absolute bottom-4 right-4 bg-black/60 backdrop-blur-sm rounded-lg px-3 py-1.5">'
    '<span class="text-xs font-medium text-white">1 / 5</span></div></div>'
    '<div class="px-4 py-3 border-t border-neutral-100">'
    '<div class="grid grid-cols-5 md:grid-cols-6 gap-2">'
    '<div class="relative aspect-square rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-[#4654CD] ring-2 ring-[#4654CD]/20" tabindex="0" style="transform: none;">'
    '<img alt="Laptop Lenovo frontal" class="w-full h-full object-contain p-1.5 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg"></div>'
    '<div class="relative aspect-square rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0" style="transform: none;">'
    '<img alt="Laptop HP vista lateral" class="w-full h-full object-contain p-1.5 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad8af9ed1fbf48ea397396_hp15.png"></div>'
    '<div class="relative aspect-square rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0" style="transform: none;">'
    '<img alt="Laptop ASUS en escritorio" class="w-full h-full object-contain p-1.5 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad78aca11478d9ed058463_laptop_asus_x515ea.jpg"></div>'
    '<div class="relative aspect-square rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0" style="transform: none;">'
    '<img alt="Laptop Dell para estudios" class="w-full h-full object-contain p-1.5 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7ac27cd445765564b11b_Dell%201505.jpg"></div>'
    '<div class="relative aspect-square rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0" style="transform: none;">'
    '<img alt="Laptop Hyundai portatil" class="w-full h-full object-contain p-1.5 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad79b64b6011e52725b3a7_hyndai_hybook.png"></div>'
    '</div></div>'
)

NEW = (
    '<div class="flex gap-3 p-3">'
    '<div class="flex flex-col gap-2 flex-shrink-0">'
    '<div class="w-16 h-16 relative rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-[#4654CD] ring-2 ring-[#4654CD]/20" tabindex="0">'
    '<img alt="Laptop Lenovo frontal" class="w-full h-full object-contain p-1 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg"></div>'
    '<div class="w-16 h-16 relative rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0">'
    '<img alt="Laptop HP vista lateral" class="w-full h-full object-contain p-1 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad8af9ed1fbf48ea397396_hp15.png"></div>'
    '<div class="w-16 h-16 relative rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0">'
    '<img alt="Laptop ASUS en escritorio" class="w-full h-full object-contain p-1 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad78aca11478d9ed058463_laptop_asus_x515ea.jpg"></div>'
    '<div class="w-16 h-16 relative rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0">'
    '<img alt="Laptop Dell para estudios" class="w-full h-full object-contain p-1 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7ac27cd445765564b11b_Dell%201505.jpg"></div>'
    '<div class="w-16 h-16 relative rounded-lg overflow-hidden border-2 cursor-pointer transition-all border-neutral-200 hover:border-neutral-300" tabindex="0">'
    '<img alt="Laptop Hyundai portatil" class="w-full h-full object-contain p-1 bg-white" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad79b64b6011e52725b3a7_hyndai_hybook.png"></div>'
    '</div>'
    '<div class="flex-1 relative cursor-zoom-in group overflow-hidden rounded-xl">'
    '<div class="relative w-full h-full" style="opacity: 1;">'
    '<img alt="Laptop Lenovo frontal" class="w-full h-full object-contain p-8 transition-transform duration-200" loading="lazy" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg" style=""></div>'
    '<div class="absolute top-4 right-4 bg-white/80 backdrop-blur-sm rounded-lg px-3 py-2 flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">'
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-zoom-in w-4 h-4 text-neutral-600" aria-hidden="true">'
    '<circle cx="11" cy="11" r="8"></circle><line x1="21" x2="16.65" y1="21" y2="16.65"></line><line x1="11" x2="11" y1="8" y2="14"></line><line x1="8" x2="14" y1="11" y2="11"></line></svg>'
    '<span class="text-xs font-medium text-neutral-700">Hover para zoom</span></div>'
    '<div class="absolute bottom-4 left-4 bg-black/60 backdrop-blur-sm rounded-lg px-3 py-1.5 flex items-center">'
    '<span class="text-[10px] uppercase tracking-wider text-white/80 leading-none">Imagen referencial</span></div>'
    '<div class="absolute bottom-4 right-4 bg-black/60 backdrop-blur-sm rounded-lg px-3 py-1.5">'
    '<span class="text-xs font-medium text-white">1 / 5</span></div>'
    '</div>'
    '</div>'
)

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Gallery restructured.")
else:
    print("ERROR: OLD string not found in file.")
    # Try to find a partial match for debugging
    marker = '<div class="relative aspect-square cursor-zoom-in group overflow-hidden">'
    if marker in content:
        print("Marker found - partial match exists")
    else:
        print("Marker NOT found either")
