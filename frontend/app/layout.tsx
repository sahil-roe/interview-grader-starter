import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Interview Grader",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen bg-gray-50">
          <header className="bg-white border-b border-gray-200 px-6 py-4">
            <div className="max-w-5xl mx-auto">
              <span className="text-base font-semibold text-gray-900">
                Interview Grader
              </span>
            </div>
          </header>
          <main className="max-w-5xl mx-auto px-6 py-8">{children}</main>
        </div>
      </body>
    </html>
  );
}
