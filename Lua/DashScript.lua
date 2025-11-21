local Player = game.Players.LocalPlayer
local character = Player.Character or Player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")
local root = character:WaitForChild("HumanoidRootPart")

-- Cria animação de dash
local dashAnimation = Instance.new("Animation")
dashAnimation.AnimationId = "rbxassetid://107159771235560" -- tua animação
local animator = humanoid:FindFirstChildOfClass("Animator") or Instance.new("Animator", humanoid)
local dashTrack = animator:LoadAnimation(dashAnimation)

-- Config do dash
local canDash = true
local DashForce = 100
local DashTime = 0.25
local cooldown = 2

function onDash()
	if not canDash then return end
	canDash = false

	-- toca animação
	dashTrack:Play()
	dashTrack.Priority = Enum.AnimationPriority.Action

	-- aplica movimento
	local bv = Instance.new("BodyVelocity")
	bv.MaxForce = Vector3.new(50000, 0, 50000)
	bv.Velocity = root.CFrame.LookVector * DashForce
	bv.Parent = root

	-- reseta velocidade horizontal antes do impulso (evita empilhar)
	root.AssemblyLinearVelocity = Vector3.new(0, root.AssemblyLinearVelocity.Y, 0)

	task.wait(DashTime)

	bv:Destroy()

	if dashTrack.IsPlaying then
		dashTrack:Stop()
	end

	task.wait(cooldown)
	canDash = true
end

game:GetService("UserInputService").InputBegan:Connect(function(input, processed)
	if processed then return end
	if input.KeyCode == Enum.KeyCode.Q then
		onDash()
	end
end)
