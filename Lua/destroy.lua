local DropperPartsFolder = script.Parent.Parent.Parent.DropperParts

while wait(2) do
	local NewPart = Instance.new("Part",DropperPartsFolder)
	NewPart.Position = script.Parent.SpawnPart.Position
	NewPart.Size = Vector3.new(1,1,1)
	
    NewPart:AddTag("Bloco")

	local CashValues = Instance.new("NumberValue",NewPart)
	CashValues.Value = 1
	CashValues.Name = "CashValue"
end
