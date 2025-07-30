import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar, PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';
import { Card, CardContent } from "@/components/ui/card";

const sampleForecast = [
  { date: '2025-07-10', predicted: 45 },
  { date: '2025-07-11', predicted: 48 },
  { date: '2025-07-12', predicted: 52 },
  { date: '2025-07-13', predicted: 38 },
  { date: '2025-07-14', predicted: 44 },
  { date: '2025-07-15', predicted: 50 },
  { date: '2025-07-16', predicted: 55 },
];

export default function Dashboard() {
  const [selectedTab, setSelectedTab] = useState("supplier");

  const renderChart = () => {
    switch (selectedTab) {
      case "supplier":
        return (
          <Card className="p-4">
            <CardContent>
              <h2 className="text-xl font-bold mb-2">Supplier Upload Portal</h2>
              <p>Upload interface with fields: Product Name, Category, Quantity, Price, etc.</p>
            </CardContent>
          </Card>
        );

      case "buyer":
        return (
          <Card className="p-4">
            <CardContent>
              <h2 className="text-xl font-bold mb-2">Buyer Dashboard</h2>
              <p>Product selection and current stock details with alert if low.</p>
            </CardContent>
          </Card>
        );

      case "demand":
        return (
          <Card className="p-4">
            <CardContent>
              <h2 className="text-xl font-bold mb-2">Demand Forecasting</h2>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={sampleForecast}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="date" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="predicted" stroke="#8884d8" name="Predicted Demand" />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        );

      case "analytics":
        return (
          <Card className="p-4">
            <CardContent>
              <h2 className="text-xl font-bold mb-2">Analytics and Reporting</h2>
              <p>Charts: Bar for supermarket sales, Pie for category distribution.</p>
            </CardContent>
          </Card>
        );

      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="flex space-x-4 mb-4">
        <button className="btn" onClick={() => setSelectedTab("supplier")}>Supplier Upload</button>
        <button className="btn" onClick={() => setSelectedTab("buyer")}>Buyer Dashboard</button>
        <button className="btn" onClick={() => setSelectedTab("demand")}>Demand Forecast</button>
        <button className="btn" onClick={() => setSelectedTab("analytics")}>Analytics</button>
      </div>
      {renderChart()}
    </div>
  );
}
