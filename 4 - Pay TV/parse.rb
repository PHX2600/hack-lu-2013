File.open("output", "r") do |infile|
    while (line = infile.gets)
	puts line.first
	if line.include? "{"
		workingstart = line.split(%r{start": })
#		puts workingstart[]
		startval = workingstart[1].split(%r{,})
#		puts startval[0]
		secondstart = line.split(%r{end": })
		secval = secondstart[1].split(%r{,})
#		puts secval[0]
		puts (secval[0].to_f - startval[0].to_f)

	end	
    end
end
