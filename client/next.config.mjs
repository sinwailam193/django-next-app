/** @type {import('next').NextConfig} */
const nextConfig = {
    output: "export",
    async rewrites() {
        return [
            {
                source: "/api/:path*",
                destination: "http://localhost:8000/api/:path*",
            },
        ];
    },
};

export default nextConfig;
