from conans import CMake, ConanFile, tools
import os

class VulkanHeadersConan(ConanFile):
    name = "vulkan-headers"
    version = "1.2.131"
    url = "https://github.com/KhronosGroup/Vulkan-Headers"
    description = "Vulkan Header files and API registry"
    
    settings = "os", "compiler", "build_type", "arch"
    
    
    no_copy_source = True
    
    def source(self):
        tools.get(
            f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{self.version}.tar.gz")
    
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=os.path.join(
            self.source_folder, f"Vulkan-Headers-{self.version}"))
        cmake.build()
    
    def package(self):
        cmake = CMake(self)
        cmake.install(build_dir=self.build_folder)
    
    def package_info(self):
        self.user_info.VULKAN_REGISTRY_PATH = os.path.join(
            self.package_folder, "share", "vulkan", "registry")
